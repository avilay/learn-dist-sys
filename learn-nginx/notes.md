# Nginx

Refs:
  * [Beginners Guide](https://nginx.org/en/docs/beginners_guide.html)

## Start, Stop, and Reload
```shell
# This will start nginx as a daemon
nginx

# For fast shutdown
nginx -s stop

# For graceful shutdown
nginx -s quit

# To reload all the config files
nginx -s reload
```

Default locations for logs (both access.log and error.log) is at `/var/log/nginx/`.

## Config
The default config is located at `/etc/nginx/nginx.conf`. At the end it will typically include entries - 

```
include /etc/nginx/conf.d/*.conf;
include /etc/nginx/sites-enabled/*;
```

`sites-enabled` directory usually contains symbolic link to files in `sites-available` directory. I'll see a `sites-available/default` symlinked to `sites-enabled/default`. It creates a default server block (see below for what this means).

Configs are the heart of nginx. There is a top level section called http which needs to have at least one sub-section called server (also referred to as "virtual servers" in some documentation).

### As a Content Web Server

Below is a very simple config -

```
http {
    server {
        root /www

        location /traffic {
            root /www/data;
            # First attempt to serve request as file, then
			# as directory, then fall back to displaying a 404.
			try_files $uri $uri/ =404;
        }

        location /media {
        	# First attempt to serve request as file, then
			# as directory, then fall back to displaying a 404.
			try_files $uri $uri/ =404;
        }
    }
}
```

The above config defines a single virtual server that can respond to two types of URLs -
  * http://example.org/traffic/us/seattle.html
  * http://example.org/media/pictures/python.png

In the first case, the path matches the `/traffic` location directive. Ngnix will prepend the root path to the URL (minus the host name), so it will serve whatever it finds at `/www/data/traffic/us/seattle.html`. In the second case, the URL will match the `/media` location directive. Nginx will server whatever it finds at `/www/media/pictures/profile.png`. Because there is no root attribute for this location, nginx falls back to the server's root attribute.

Each of "events", "http", "server", etc. are called directives or modules. I can find the list all directives [here](https://nginx.org/en/docs/dirindex.html). E.g, the documentation for the "server" directive can be found [here](https://nginx.org/en/docs/http/ngx_http_core_module.html#server).

### As a Reverse Proxy

Here is a simple config -

```
http {
    server {
        listen 80;
        server_name blogs.avilay.rocks
        location / {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	        proxy_set_header Host $http_host;
	        proxy_redirect off;
            proxy_pass http://127.0.0.1:5000
        }
    }
}
```

Nginx itself is listening on port 80 for hostname blogs.avilay.rocks. So any request to `http://blogs.avilay.rocks` will be handled by this server module. There can be multiple server modules listening on port 80 but different server names. That is how I can get nginx to host multiple apps. The `proxy_set_header` directives are so that the app server actually hosting blogs.avilay.rocks, which will be a Flask or a NodeJS application, will actually get the host name that the user has used. Turning off `proxy_redirect` is so that nginx does not do something too clever with redirects. Typically I'd want the app server to handle that.

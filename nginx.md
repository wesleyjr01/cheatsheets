### Start / Install Nginx:
https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04
```
$ sudo apt install nginx
$ sudo ufw allow 'Nginx HTTP'
$ systemctl status nginx
$ /etc/nginx/sites-enabled
$ /etc/nginx/sites-available
```

### Setting Up Server Blocks

```
$ sudo mkdir -p /var/www/example.com/html
$ sudo chown -R $USER:$USER /var/www/example.com/html
$ sudo chmod -R 755 /var/www/example.com
$ nano /var/www/example.com/html/index.html
	<html>
	    <head>
		<title>Welcome to Example.com!</title>
	    </head>
	    <body>
		<h1>Success!  The example.com server block is working!</h1>
	    </body>
	</html>
$ sudo nano /etc/nginx/sites-available/example.com
	server {
		listen 80;
		listen [::]:80;

		root /var/www/example.com/html;
		index index.html index.htm index.nginx-debian.html;

		server_name example.com www.example.com;

		location / {
			try_files $uri $uri/ =404;
		}
	}
$ sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
$ sudo nano /etc/nginx/nginx.conf
	...
	http {
	    ...
	    server_names_hash_bucket_size 64;
	    ...
	}
	...
$ sudo nginx -t
$ sudo systemctl restart nginx
```

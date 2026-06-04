# Use nginx to serve static files
FROM nginx:alpine

# Copy all frontend files to nginx directory
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]

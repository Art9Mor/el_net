# Electronic store ElNet  

Online platform for electronics retail chain

## Description

Here is an API service for a network selling electronics.  
This project provides an opportunity to get acquainted with various types of electrical appliances and sellers right up to the manufacturing plant.

## Instructions  

1. Clone the repository  

   - https

          git clone https://github.com/Art9Mor/el_net.git

   - ssh

          git clone git@github.com:Art9Mor/el_net.git

2. Set up environment variables

    - Create an `.env` file in the project root
    - Copy the contents from ".env.sample" to the file you created
    - Fill in the variable values with your data
   
   Variable values:

        
        DJANGO_SECRET_KEY=write_your_secret_key_for_django_project

        DEBUG=debug_mode (must be in "False" mode if used in a production environment)
        DJANGO_ALLOWED_HOSTS=write_here_hosts_to_allow_them
        
        # for runserver
        POSTGRES_DB=your_database_name
        POSTGRES_USER=your_database_user
        POSTGRES_PASSWORD=your_database_password
        
        # for docker compose
        HOST=your_host_name
        PORT=your_release_port
        
        LANGUAGE_CODE=chose_your_language
        TIME_ZONE=your_timezone
        

3. 
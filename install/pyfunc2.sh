#!/usr/bin/env python3
import os
import sys
import subprocess
import platform

def run_command(command):
    """Execute a shell command and return its output."""
    print(f"Running: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               universal_newlines=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(f"Error output: {e.stderr}")
        return None

def detect_distro():
    """Detect the Linux distribution."""
    # Try to use /etc/os-release first
    if os.path.exists('/etc/os-release'):
        with open('/etc/os-release', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('ID='):
                    return line.split('=')[1].strip().strip('"').lower()

    # Fallback to platform module
    return platform.linux_distribution()[0].lower()

def install_system_dependencies(distro):
    """Install system dependencies based on the detected distribution."""
    print(f"Detected Linux distribution: {distro}")

    # Debian-based systems (Ubuntu, Debian, etc.)
    if distro in ['debian', 'ubuntu', 'linuxmint', 'pop']:
        run_command("sudo apt-get update")
        run_command("sudo apt-get install -y imagemagick poppler-utils")

    # Red Hat-based systems (RHEL, CentOS)
    elif distro in ['rhel', 'centos', 'fedora']:
        if distro == 'fedora':
            run_command("sudo dnf install -y ImageMagick poppler-utils")
        else:
            run_command("sudo yum install -y epel-release")
            run_command("sudo yum install -y ImageMagick poppler-utils")

    # Arch Linux
    elif distro in ['arch', 'manjaro']:
        run_command("sudo pacman -Sy --noconfirm imagemagick poppler")

    # openSUSE
    elif distro in ['opensuse', 'suse']:
        run_command("sudo zypper install -y ImageMagick poppler-tools")

    else:
        print(f"Unsupported distribution: {distro}")
        print("Please install ImageMagick and Poppler manually.")
        return False

    return True

def install_python_dependencies():
    """Install required Python packages."""
    print("Installing Python dependencies...")
    run_command("pip install wand pdf2image pillow")

def main():
    """Main function to install all dependencies."""
    print("Starting installation of pyfunc2 dependencies...")

    # Check if running as root or with sudo
    if os.geteuid() != 0:
        print("Warning: Some commands may require sudo privileges.")

    # Detect and install system dependencies
    distro = detect_distro()
    if install_system_dependencies(distro):
        print("System dependencies installed successfully.")

    # Install Python dependencies
    install_python_dependencies()
    print("Python dependencies installed successfully.")

    print("\nAll dependencies for pyfunc2 have been installed.")
    print("You can now use the pyfunc2 package in your projects.")

if __name__ == "__main__":
    main()

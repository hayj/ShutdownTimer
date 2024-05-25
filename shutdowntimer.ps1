# Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
# choco install git
# choco install -y python3
# pip install --trusted-host pypi.python.org tk

# Define the repository URL and temporary directory
$repoURL = "https://github.com/hayj/ShutdownTimer"
$tempDir = [System.IO.Path]::Combine([System.IO.Path]::GetTempPath(), [System.IO.Path]::GetRandomFileName())

# Create the temporary directory
New-Item -ItemType Directory -Path $tempDir

# Download the repository
Write-Output "Cloning the repository..."
git clone $repoURL $tempDir

# Navigate to the downloaded directory
Set-Location -Path $tempDir

# Execute the command "shutdowntimer"
Write-Output "Executing 'shutdowntimer' command..."
python3.12.exe $tempDir\shutdowntimer\main.py

if test -d ~/.bin/; then
	echo "[+] ~/.bin/ exists"
else
	echo "[-] ~/.bin/ does note exist. Creating..."
	mkdir ~/.bin/
	echo "[+] ~/.bin/ created"
	echo 'export PATH="~/.bin:$PATH"' >> ~/.bashrc
	source ~/.bashrc
	echo "[+] ~/.bin/ added to PATH"
fi

# Copy files to .bin
echo "[-] Copying files to ~/.bin"
mkdir ~/.bin/.defang_source/
cp -rf ./* ~/.bin/.defang_source/
echo "[+] Files copied to ~/.bin"

# Make the bash script to run the main file
echo "[-] Making defang executable..."
touch ~/.bin/defang
echo "#!/bin/bash" >> ~/.bin/defang
echo "~/.bin/.defang_source/main.py \$1 \$2" >> ~/.bin/defang
sudo chmod +x ~/.bin/defang

echo "[+] defang is ready for use"

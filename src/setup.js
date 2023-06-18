const { exec } = require('child_process');

const packages = ['fluent-ffmpeg', 'node-speech', '@google-cloud/speech', 'openai', 'express', 'body-parser'];

packages.forEach(package => {
    exec(`npm install ${package}`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error installing ${package}: ${error}`);
            return;
        }
        console.log(`Installed ${package}: ${stdout}`);
        console.error(`stderr: ${stderr}`);
    });
});
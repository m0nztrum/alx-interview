#!/usr/bin/node

// Load request module
const request = require('request');
const movId = process.argv[2];

function fetchCharacters() {
    const url = `https://swapi-api.alx-tools.com/api/films/${movId}`;

    request(url, async function (error, response, body) {
        if (error) {
            console.error(Error);
            return;
        }

        const film = JSON.parse(body);
        for (const characterUrl of film.characters) {
            await new Promise((resolve, reject) => {
                request(characterUrl, function (error, response, body) {
                    if (error) {
                        reject(error);
                        return;
                    }
                    const character = JSON.parse(body);
                    console.log(character.name);
                    resolve();
                });
            });
        }
    });
}

if (movId) {
    fetchCharacters();
} else {
    console.log('Usage: ./0-starwars_characters.js "id"');
}

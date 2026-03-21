async function loadTracks(query = "") {
    const tableBody = document.getElementById("tracks-table-body");

    if (!tableBody) return;

    tableBody.innerHTML = `
        <tr>
            <td colspan="4">Loading...</td>
        </tr>
    `;

    let url = "/api/tracks/";
    if (query) {
        url += `?q=${encodeURIComponent(query)}`;
    }

    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }

        const tracks = await response.json();

        if (tracks.length === 0) {
            tableBody.innerHTML = `
                <tr>
                    <td colspan="4">No tracks found</td>
                </tr>
            `;
            return;
        }

        tableBody.innerHTML = tracks.map(track => `
            <tr>
                <td><a href="/tracks/${track.id}/">${track.title}</a></td>
                <td>${track.artist.name}</td>
                <td>${track.album.title}</td>
                <td>${track.popularity}</td>
            </tr>
        `).join("");

    } catch (error) {
        console.error(error);
        tableBody.innerHTML = `
            <tr>
                <td colspan="4">Error loading tracks</td>
            </tr>
        `;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("track-search-form");
    const input = document.getElementById("track-search-input");

    if (form && input) {
        loadTracks();

        form.addEventListener("submit", (e) => {
            e.preventDefault();
            loadTracks(input.value.trim());
        });
    }
});
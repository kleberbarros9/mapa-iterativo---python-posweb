document.addEventListener("DOMContentLoaded", function() {
    // Inicializa o mapa leaflet
    var map = L.map('map').setView([-7.98526, -38.2929], 7);
    
    // Adiciona o tile base (mapa de fundo)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Função para buscar os dados via API do servidor Python (Flask)
    fetch('/api/data')
    .then(response => response.json())
    .then(data => {
        // Adiciona o GeoJSON (estado de PE) ao mapa
        L.geoJSON(data.pe_geojson, {
            style: {
                color: '#ffb825',
                weight: 2
            }
        }).addTo(map);
        
        // Adiciona os marcadores dos municípios
        data.municipios.forEach(m => {
            L.marker([m.lat, m.lng]).addTo(map)
                .bindPopup(
                    `<strong>Município:</strong> ${m.municipio}<br>
                     <strong>Apicultores:</strong> ${m.apicultores}<br>
                     <strong>Mulheres:</strong> ${m.mulheres}<br>
                     <strong>Produção anual:</strong> ${m.producao}`
                );
        });
    })
    .catch(error => console.error('Erro ao carregar dados:', error));
});

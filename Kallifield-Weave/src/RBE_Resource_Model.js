function setup() {
    createCanvas(400, 400);
    background(220);
    // Initialize resource grid (10x10)
    this.resources = Array(10).fill().map(() => Array(10).fill(50));
}

function draw() {
    background(220);
    for (let i = 0; i < 10; i++) {
        for (let j = 0; j < 10; j++) {
            fill(0, this.resources[i][j], 0); // Green for resource level
            rect(i * 40, j * 40, 40, 40);
            // Simulate equitable distribution
            if (frameCount % 60 === 0) {
                this.resources[i][j] += (75 - this.resources[i][j]) * 0.1;
            }
        }
    }
}

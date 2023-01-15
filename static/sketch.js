let nb = 100;
let p = Array(nb);

function setup() {
  canvas_w = windowWidth;
  canvas_h = windowHeight;
  title_1 = "Horror Manga";
  title_2 = "Style Transfer";
  canvas = createCanvas(canvas_w, canvas_h);
  canvas.position(0, 0);
  canvas.style("z-index", "-1");
  canvas.parent("canvas-container");

  for (let i = 0; i < nb; i++) {
    p[i] = new Particle(random(0, canvas_w), random(0, canvas_h));
  }
}

function draw() {
  background(0);
  textSize(130);
  textFont("Lacquer");
  noStroke();
  fill(255, 255, 255, 51);
  textAlign(CENTER);
  text(title_1, canvas_w / 2, canvas_h / 3.2);
  textSize(55);
  text(title_2, canvas_w / 2, canvas_h / 2.5);

  stroke(255, 255, 255, 25);
  strokeWeight(random(1, 5));
  noFill();
  for (let i = 0; i < nb; i++) {
    p[i].draw();
  }
}

class Particle {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.r = random(canvas_w / 20, canvas_w / 5);
    this.vr = random(-2, 2);
  }

  draw() {
    this.r = this.r - this.vr;
    ellipse(this.x, this.y, this.r, this.r);
    if (this.r < 0 || this.r > canvas_w / 2) {
      this.r = random(canvas_w / 20, canvas_w / 4);
    }
  }
}

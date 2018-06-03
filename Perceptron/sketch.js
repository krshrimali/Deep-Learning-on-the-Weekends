// describe a sample function : y = mx + c
// this fits the data

let training = new Array(2000);
let ptron;
let count = 0;

let xmin = -1;
let ymin = -1;
let xmax = 1;
let ymax = 1;


function f(x) {
    let y = x * x;
    return y;
}

function setup() {
    createCanvas(400, 400); // create canvas 

    ptron = new Perceptron(3, 0.01); // change learning rate to 0.1
    // Params: 
    // 1) 3 inputs, x y and bias 
    // 2) learning rate - 0.001

    // create random set of training points and calculate known
    // answer
    for (let i = 0; i < training.length; i++) {
        let x       = random(xmin, xmax);
        let y       = random(ymin, ymax);
        let output  = 1; // ground truth
        
        training[i] = {
            input : [x, y, 1],
            output: output
        };
    }
}

function draw() {
    background(0);

    // draw the line based on current weights
    // w[0] * x + w[1] * y + w[2] = 0
    // y = (-w[2] - w[0] * x)/w[1]
    stroke(255);
    strokeWeight(2);

    let weights = ptron.getWeights();
    x1 = xmin;
    y1 = (-weights[2] - weights[0] * x1) / weights[1];
    x2 = xmax;
    y2 = (-weights[2] - weights[0] * x2) / weights[1];
    
    // map 1st argument having range (2nd, 3rd) to (4th, 5th) arguments
    // more details: https://www.youtube.com/watch?v=nicMAoW6u1g/ 

    x1 = map(x1, xmin, xmax, 0, width);
    x2 = map(x2, xmin, xmax, 0, width);
    y1 = map(y1, ymin, ymax, height, 0);
    y2 = map(y2, ymin, ymax, height, 0);
	line(x1, y1, x2, y2);

    ptron.train(training[count].input, training[count].output);

    count = (count + 1) % training.length; 

    for(let i = 0; i < count; i++) {
        stroke(255);
        strokeWeight(1);
        fill(255);
        let guess = ptron.feedforward(training[i].input);
        if(guess > 0) noFill();

        let x = map(training[i].input[0], xmin, xmax, 0, width);
        let y = map(training[i].input[1], ymin, ymax, height, 0);
        ellipse(x, y, 8, 8);
    }
}


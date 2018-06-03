class Perceptron {
    constructor(n, c) {
        this.weights = new Array(n);

        for (let i = 0; i < this.weights.length; i++) {
            this.weights[i] = random(-1, 1);
        }
        this.c = c; // learning rate
    }

    train(inputs, labels) {
        let guess = this.feedforward(inputs);
        // now back prop it
        // first calculate error
        // MSE or Error = output (desired) - output (guessed)
        //
        let error = labels - guess; 
        for(let i = 0; i < this.weights.length; i++) {
            this.weights[i] += this.c * error * inputs[i]; 
        }
    }

    feedforward(inputs) {
        let sum = 0; 
        for (let i = 0; i < this.weights.length; i++) {
            sum += inputs[i] * this.weights[i]; 
        }
        // why not add bias? 
        // check
        return this.activate(sum);
    }

    activate(sum) {
        // sigmoid
        if(sum > 0) return 1;
        else return -1;
    }
    
    getWeights() {
        return this.weights;
    }
}

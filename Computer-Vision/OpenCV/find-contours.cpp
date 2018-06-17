#include <iostream>
#include "opencv2/opencv.hpp"

using namespace std;

// declare images
// im - input image
// imCanny - output image
// display - dynamic display
cv::Mat im, imCanny, display; 

// define params:
// lowthreshold, high threshold
// aperture size
// blur
int thresh, maxThreshold = 3 * 255; 

// random number generator with seed
cv::RNG rng(12345);

// callback - slider
void callback(int, void*);


int main(int argc, char const *argv[])
{
    cv::string filename("threshold.jpg"); // default input image
    // to use non-default image
    if(argc > 1) {
        filename = argv[1];
    }
    
    return 0;
}

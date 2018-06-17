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
    string filename("threshold.jpg"); // default input image
    // to use non-default image
    if(argc > 1) {
        filename = argv[1];
    }

    im = cv::imread(filename, cv::IMREAD_GRAYSCALE); // read as grayscale
    // resize in case the image is big
    cv::resize(im, im, cv::Size(im.cols * 0.5, im.rows * 0.5), 0, 0);
    // display original image
    cv::namedWindow("Contours", cv::WINDOW_AUTOSIZE);
    cv::imshow("original", im);

    cv::createTrackbar("Canny Thresh:", "Contours", &thresh, maxThreshold, callback); 
    callback(0, 0);
    cv::waitKey(0);
    return 0;
}

void callback(int, void*) {
    vector<vector<cv::Point>> contours;
    
    vector<cv::Vec4i> hierarchy;

    cv::Canny(im, imCanny, thresh, thresh*2, 3);
    cv::findContours(imCanny, contours, hierarchy, cv::RETR_TREE, cv::CHAIN_APPROX_SIMPLE);

    if(display.empty()) {
        display = cv::Mat::zeros(imCanny.size(), CV_8UC3);
    }
    else {
        display.setTo(cv::Scalar(0, 0, 0));
    }

    for(size_t i = 0; i < contours.size(); i++) {
        cv::Scalar color = cv::Scalar(rng.uniform(0, 255), rng.uniform(0, 255), rng.uniform(0, 255));
        cv::drawContours(display, contours, int(i), color, 2);
    }
    cv::imshow("Contours", display);
}
# Summary
install tensorflow on M1  
apple provides MacOS-optimized Tensorflow and this supports both M1 and intel Macs.  

## [Mac-optimized TensorFlow from Apple](https://github.com/apple/tensorflow_macos#mac-optimized-tensorflow-and-tensorflow-addons)
Native hardware acceleration is supported on M1 Macs and Intel-based Macs through Apple’s [ML Compute](https://developer.apple.com/documentation/mlcompute) framework.
![](https://1.bp.blogspot.com/--pH8VjDtKrg/X7VcRHJ6e1I/AAAAAAAADvU/MXdxFn-Fjx0AxPIWp35JQCP93S9ky-SDACLcBGAsYHQ/s0/MacBook%2BPro%2B1.png)  
https://blog.tensorflow.org/2020/11/accelerating-tensorflow-performance-on-mac.html

## TensorFlow install
1. M1 Mac
    1. M1 TensorFlow
        1. conda  
           * Guidance: [https://github.com/apple/tensorflow_macos/issues/153](https://github.com/apple/tensorflow_macos/issues/153)  
           * It's said that Anaconda has some incompatible packages so Miniforge3(similar to miniconda) should be used.
             I think, but if that's the only reason, Anaconda could be acceptable by using empty conda env but didn't test.
        2. venv  
           * Guidance: [https://github.com/apple/tensorflow_macos](https://github.com/apple/tensorflow_macos)
        
    2. Intel TensorFlow on rosetta2
        1. conda
        2. venv  
            Guidance: [https://www.tensorflow.org/install/source](https://www.tensorflow.org/install/source) (build from source)  
            1. get Xcode
            2. install Bazel (install from binary for easy version control)  
               * Guidance: [bazel site](https://docs.bazel.build/versions/master/install-os-x.html#install-with-installer-mac-os-x)  
               * Check bazel version based on TF version you want to build([link](https://www.tensorflow.org/install/source#cpu))
            3. Build and Install
    

2. Intel Mac 

# Test
M1 TF: v.2.4.0-rc0  
Intel TF: v.2.5.0

## On M1 Mac, M1 TF vs Intel TF via Rosetta2
test case: mnist fashion data with code from tensorflow.org  
training time per epoch: M1 12 sec vs Intel 24 sec

## M1 TF, using cpu vs gpu

training time per epoch: cpu 12 sec vs gpu 55 sec



# NPU

NPU SPECIFICATIONS:-

RV1103 specs:-
----------------
Processor: Cortex A7@1.2GHz + RISC-V

NPU: 0.5TOPS, supports int4, int8 and int16

Memory: 64MB DDR2

RK3588 Specs:-
--------------


*6TOPS@int8

*support int4/int8/FP16/BF16/TF32

*support deep learning  frameworks :-TensorFlow,Caffe,
     Tflite,Pytorch,Onnx NN,Android NN,etc

*Memory:-4GB


SETUP STEPS:-
------------
sudo apt install python3-pip


harish@DESKTOP-JCC3N1V:/mnt/c/Users/haris/Downloads/p$ pip3 install -r rknn-toolkit2/rknn-toolkit2/packages/requirements_cp310-1.6.0.txt


https://www.scs.stanford.edu/~zyedidia/docs/rockchip/


https://github.com/FanX-Tek/rk3588-TRM-and-Datasheet/blob/master/Rockchip_RK3588S_Datasheet_V1.3-20220310.pdf



Network connection test:-
https://www.youtube.com/watch?v=9rojGc7OKao

https://www.youtube.com/watch?v=ILmedtqtrQ8&t=79s

https://www.youtube.com/watch?v=N_l7rZeAxKs

https://www.youtube.com/watch?v=DMWD7wfhgNY&t=102s

RK3588 details:-
-----------------



installation sucefull with 

pip install rknn-toolkit2 -i https://mirrors.aliyun.com/pypi/simple/



(rknn) ubuntu@DESKTOP-MLTHVPE:/mnt/c/Users/haris/Downloads/p/Projects/p/rknn-toolkit2$ pip install -r rknn-toolkit2/packages/requirements_cp39-1.6.0.txt




ADB is not working

winscp is successfule with transfering data from pc to target board


wsl --shutdown Ubuntu

g++ set using windows:- setx PATH "%PATH%;D:\mingw64\bin"

tasks.json

{
  "version": "2.0.0",
  "tasks": [
    {
      "type": "shell",
      "label": "C/C++: g++.exe build active file",
      "command": "D:/mingw64/bin/g++.exe",
      "args": [
        "-fdiagnostics-color=always",
        "-g",
        "${file}",
        "-o",
        "${fileDirname}\\${fileBasenameNoExtension}.exe"
      ],
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "problemMatcher": ["$gcc"]
    }
  ]
}





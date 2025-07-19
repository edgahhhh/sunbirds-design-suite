% SETUP.m
% Author: Edgar Hernandez
% Date: June 13, 2025
% ------------
% Purpose:
%   Script to setup project for developmental use with matlab.

clear
clc
setupPaths

function setupPaths
trunkPath = pwd;
addpath(genpath(pwd))
cd (trunkPath)
end
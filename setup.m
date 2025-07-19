% SETUP.m
% Author: Edgar Hernandez
% Date: June 13, 2025
% ------------
% Purpose:
%   Script to setup project for developmental use with matlab.
%   Only run in main path, can be done directly from command window
%       While in subnirds-design-suite run >> setup

clear
clc
setupPaths

function setupPaths
trunkPath = pwd;
addpath(genpath(pwd))
cd (trunkPath)
end
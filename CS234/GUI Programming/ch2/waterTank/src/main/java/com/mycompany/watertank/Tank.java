/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.watertank;

/**
 *
 * @author CEHVAREE
 */
public class Tank {
    
    private double length = 0.0;
    private double width = 0.0;
    private double height = 0.0;
    private double area = 0.0;
    private double volume = 0.0;

    public Tank() {
    }

    public double getLength() {
        return length;
    }

    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }

    public void setLength(double length) {
        this.length = length;
    }

    public void setWidth(double width) {
        this.width = width;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public double getArea() {
        area = (length * width) + 2*(length * height) + 2*(width * height);
        return area;
    }

    public double getVolume() {
        volume = length * width * height;
        return volume;
    }
    
   
}

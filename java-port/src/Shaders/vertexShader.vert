#version 400 core

in vec3 position;

out vec3 color;

uniform mat4 transMatrix;

void main(void){

    gl_Position = vec4(position.xyz,1.0);
    color = vec3(position.x+0.5,1.0,position.y+0.5);

}

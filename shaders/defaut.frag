#version 330 core
layout (location = 0) out vec4 fragColor;
in vec2 uv_0;
in vec4 gl_FragCoord;

void main(){

    // vec3 color = vec3(gl_FragCoord.y/450.0,1-gl_FragCoord.x/800.0,gl_FragCoord.x/800.0);
    vec3 color = vec3(uv_0,sin(gl_FragCoord.x/6.));
    // vec3 color = vec3(1.0,0,0);
    fragColor = vec4(color , 1.0);
}
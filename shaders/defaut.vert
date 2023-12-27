#version 330 core

layout(location = 0) in vec2 text_coord;
layout(location = 1) in vec3 position;

out vec2 uv_0;

uniform mat4 m_proj;
uniform mat4 m_view;

void main() {
    uv_0=text_coord;
    gl_Position = m_proj*m_view*vec4(position,1.0);
}
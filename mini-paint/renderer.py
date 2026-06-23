from __future__ import annotations

from typing import Iterable

import numpy as np
from OpenGL.GL import (
    GL_ARRAY_BUFFER,
    GL_COLOR_BUFFER_BIT,
    GL_FLOAT,
    GL_FRAGMENT_SHADER,
    GL_LINE_LOOP,
    GL_LINE_STRIP,
    GL_LINES,
    GL_STATIC_DRAW,
    GL_TRIANGLES,
    GL_TRIANGLE_FAN,
    GL_VERTEX_SHADER,
    glBindBuffer,
    glBindVertexArray,
    glBufferData,
    glClear,
    glClearColor,
    glCreateProgram,
    glCreateShader,
    glDeleteBuffers,
    glDeleteProgram,
    glDeleteShader,
    glDeleteVertexArrays,
    glDrawArrays,
    glEnableVertexAttribArray,
    glGenBuffers,
    glGenVertexArrays,
    glGetUniformLocation,
    glLineWidth,
    glShaderSource,
    glCompileShader,
    glAttachShader,
    glLinkProgram,
    glUseProgram,
    glVertexAttribPointer,
    glViewport,
    glUniformMatrix3fv,
    glUniformMatrix4fv,
    glUniform3f,
)

from .math_utils import Vec2, identity3, to_gl_mat3, to_gl_mat4, vec2
from .shapes import Shape, ShapeKind
from .viewport import Viewport

    
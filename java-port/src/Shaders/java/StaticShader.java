package Shaders.java;

import org.joml.Matrix4f;

public class StaticShader extends ShaderProgram {

    private static final String VERTEX_FILE = "src/Shaders/vertexShader.vert";
    private static final String FRAG_FILE = "src/Shaders/fragmentShader.frag";

    private int location_transformationMatrix;

    public StaticShader() {
        super(VERTEX_FILE, FRAG_FILE);
    }

    @Override
    protected void bindAttribs(){
        super.bindAttrib(0, "position");
    }

    @Override
    protected void getAllUniformLocations(){
        location_transformationMatrix = super.getUniformLocation("transMatrix");
    }

    public void loadTransMat(Matrix4f mat){
        super.loadMat(location_transformationMatrix, mat);
    }
}

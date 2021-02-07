package Shaders.java;

import org.lwjgl.BufferUtils;
import org.lwjgl.opengl.GL11;
import org.lwjgl.opengl.GL30;

import org.joml.Matrix4f;
import org.joml.Vector3f;
import org.lwjgl.system.MemoryStack;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.String;
import java.nio.FloatBuffer;

public abstract class ShaderProgram {

    private int programID;
    private int vertShaderID;
    private int fragShaderID;

    private static MemoryStack stack = MemoryStack.stackPush();
    private static FloatBuffer matBuffer = new Matrix4f()
            .perspective((float)Math.toRadians(45.0f), 1.0f, 0.01f, 100.0f)
            .lookAt(
                    0.0f, 0.0f, 10.0f,
                    0.0f, 0.0f, 0.0f,
                    0.0f, 1.0f, 0.0f)
            .get(stack.mallocFloat(16));

    public ShaderProgram(String vertFile, String fragFile){

        // Setup IDs
        vertShaderID = loadShader(vertFile, GL30.GL_VERTEX_SHADER);
        fragShaderID = loadShader(fragFile, GL30.GL_FRAGMENT_SHADER);
        programID = GL30.glCreateProgram();

        // Attach shaders.
        GL30.glAttachShader(programID, vertShaderID);
        GL30.glAttachShader(programID, fragShaderID);

        // Bind attributes.
        bindAttribs();

        // Link and validate program.
        GL30.glLinkProgram(programID);
        GL30.glValidateProgram(programID);

        getAllUniformLocations();
    }

    // All shader classes will have a method that gets all uniform locations.
    protected abstract void getAllUniformLocations();

    protected int getUniformLocation(String uniformName){
        return GL30.glGetUniformLocation(programID, uniformName);

    }

    ///
    /// Start the program.
    ///
    public void start(){
       GL30.glUseProgram(programID);
    }

    ///
    /// Stop the program.
    ///
    public void stop(){
        GL30.glUseProgram(0);
    }

    ///
    /// Clean up and destroy shaders for mem management.
    ///
    public void cleanUp(){

        stop();

        // Detach shaders.
        GL30.glDetachShader(programID, vertShaderID);
        GL30.glDetachShader(programID, fragShaderID);

        // Delete shaders.
        GL30.glDeleteShader(vertShaderID);
        GL30.glDeleteShader(fragShaderID);

        // Finally delete program.
        GL30.glDeleteProgram(programID);

    }

    protected abstract void bindAttribs();

    ///
    /// Take in no. of attribute list in VAO that needs to be in bind and var name in shader code to bind.
    ///
    protected void bindAttrib(int attrib, String varName){
        GL30.glBindAttribLocation(programID, attrib, varName);
    }

    protected void loadFloat(int location, float value){
        GL30.glUniform1f(location, value);
    }

   protected void loadVector(int location, Vector3f vector){
       GL30.glUniform3f(location, vector.x, vector.y, vector.z);
   }

    protected void loadBoolean(int location, boolean value){
        float toLoad = 0;
        if (value){
            toLoad = 1;
        }
        GL30.glUniform1f(location,toLoad);// Load 1 float.
    }

    protected void loadMat(int location, Matrix4f mat){
        matBuffer.flip();
        GL30.glUniformMatrix4fv(location, false, matBuffer);
    }

    // Read all lines and connect them to a long string before creating new shader.
    private static int loadShader(String file, int type){
        StringBuilder shaderSource = new StringBuilder();
        try{
            BufferedReader bfreader = new BufferedReader(new FileReader(file));
            String line;
            while ((line = bfreader.readLine()) != null){
                shaderSource.append(line).append("\n");
            }
            bfreader.close();
        } catch(IOException e){
            System.err.println("Could not read file!");
            e.printStackTrace();
            System.exit(-1);
        }
        int shaderID = GL30.glCreateShader(type);
        GL30.glShaderSource(shaderID, shaderSource);
        GL30.glCompileShader(shaderID);
        if (GL30.glGetShaderi(shaderID, GL30.GL_COMPILE_STATUS)== GL11.GL_FALSE){
            System.out.println(GL30.glGetShaderInfoLog(shaderID,500));
            System.err.println("Could not compile shader."); System.exit(-1);
        }
        return shaderID; // Returns ID to new shader created from source.
    }

}

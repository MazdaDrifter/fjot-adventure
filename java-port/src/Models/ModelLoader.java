package Models;

import Textures.Texture;
import Textures.TextureLoader;
import org.lwjgl.BufferUtils;
import org.lwjgl.stb.STBImage;
import org.lwjgl.opengl.GL30;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.FloatBuffer;
import java.nio.IntBuffer;
import java.util.ArrayList;
import java.util.List;

public class ModelLoader {

    // Lists that keep track all vbos and vaos created.
    private List<Integer> vaos = new ArrayList<Integer>();
    private List<Integer> vbos = new ArrayList<Integer>();
    private List<Integer> textures = new ArrayList<Integer>(); // All tex ids

    // Create a float array which will be our VAO.
    public RawModel loadToVao(float[] pos, int[] indices){
        int vaoID = createVAO();
        bindIndicesBuff(indices);
        storeDataInAttribList(0,pos);
        unbindVAO();
        return new RawModel(vaoID, indices.length); // Return data as a new raw model.
    }

    public int loadTexture(String filename) throws IOException {
        Textures.Texture texture = null;
        try {
            texture = TextureLoader.textureLoader("res/"+filename+".png");
        } catch (FileNotFoundException fnfe){
            fnfe.printStackTrace();
        }
        int textureID = texture.getId();
        textures.add(textureID);
        return textureID;
    }


    public void cleanUp(){
        // Loop through the vaos/vbos list and delete every buffer in them.
        for(int vao:vaos){
            GL30.glDeleteVertexArrays(vao);
        }
        for (int vbo:vbos){
            GL30.glDeleteBuffers(vbo);
        }
        for (int texture:textures){
            GL30.glDeleteTextures(texture);
        }
    }


    private int createVAO(){
        int vaoID = GL30.glGenVertexArrays();
        vaos.add(vaoID); // Add to vaos list to delete later, when game is closed.
        GL30.glBindVertexArray(vaoID);
        return vaoID;
    }

    private void storeDataInAttribList(int attribNum, float[] data){
        int vboID = GL30.glGenBuffers();
        vbos.add(vboID);
        GL30.glBindBuffer(GL30.GL_ARRAY_BUFFER, vboID); // Bind to a buffer, to be able to store data.
        FloatBuffer buffer = storeDataInFloatBuffer(data);
        // static because it is not gonna be edited anymore.
        GL30.glBufferData(GL30.GL_ARRAY_BUFFER, buffer, GL30.GL_STATIC_DRAW);
        // Where stride is distance between other data.
        GL30.glVertexAttribPointer(attribNum,3,GL30.GL_FLOAT,false,0,0);
        GL30.glBindBuffer(GL30.GL_ARRAY_BUFFER, 0); // Unbind current vbo.
    }

    private void unbindVAO(){
        // Stays bound until unbind.
        GL30.glBindVertexArray(0); // Where 0 = id.
    }

    private void bindIndicesBuff(int[] indices){
        int vboID = GL30.glGenBuffers(); // Returns id of empty vbo.
        vbos.add(vboID);
        GL30.glBindBuffer(GL30.GL_ELEMENT_ARRAY_BUFFER, vboID); // GL_ELEMENT_ARRAY_BUFFER tells openGL to use as indices buff.
        IntBuffer buff = storeDataInIntBuff(indices);
        // GL_STATIC_DRAW because it is not gonna be edited anymore.
        GL30.glBufferData(GL30.GL_ELEMENT_ARRAY_BUFFER, buff, GL30.GL_STATIC_DRAW);
    }

    private IntBuffer storeDataInIntBuff(int[] data){
        IntBuffer buff = BufferUtils.createIntBuffer(data.length);
        buff.put(data);
        buff.flip(); // Ready to be read from
        return buff;
    }


    private FloatBuffer storeDataInFloatBuffer(float[] data){
        FloatBuffer buff = BufferUtils.createFloatBuffer(data.length);
        buff.put(data);
        // Prepare buffer to be read from.
        buff.flip(); // Done writing to it.
        return buff; // return buff for using later.
    }
}

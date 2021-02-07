import Entities.RawEntity;
import Models.ModelLoader;
import Models.ModelRenderer;
import Models.RawModel;
import Models.TexturedModel;
import Shaders.java.StaticShader;
import Textures.Texture;
import Textures.TextureLoader;
import org.joml.Vector3f;
import org.lwjgl.opengl.GL;

import javax.swing.text.html.parser.Entity;

import java.io.IOException;

import static org.lwjgl.glfw.GLFW.*;
import static org.lwjgl.opengl.GL11.*;
import static org.lwjgl.opengl.GL11.GL_DEPTH_BUFFER_BIT;

public class MainGameLoop {
    public static void loop() throws IOException {
        // This line is critical for LWJGL's interoperation with GLFW's
        // OpenGL context, or any context that is managed externally.
        // LWJGL detects the context that is current in the current thread,
        // creates the GLCapabilities instance and makes the OpenGL
        // bindings available for use.
        GL.createCapabilities();

        // Set the clear color
        glClearColor(0.0f, 0.0f, 0.0f, 0.0f);

        ///
        /// Variables.
        ///

        Models.ModelLoader loader = new ModelLoader();
        Models.ModelRenderer rend = new ModelRenderer();

        StaticShader shader = new StaticShader();

        float[] vertices = {
                -0.5f,0.5f,0, //V0
                -0.5f,-0.5f,0, //V1
                0.5f,-0.5f,0, //V2
                0.5f,0.5f,0 //V3
        };

        // Order to draw triangles.
        int[] indices = {
                0,1,3,
                3,1,2
        };

        RawModel model = loader.loadToVao(vertices,indices);
        Texture tex = new Texture(loader.loadTexture("Image"));
        TexturedModel texturedModel = new TexturedModel(model, tex);
//        RawEntity entity = new RawEntity(model, new Vector3f(-1,0,0), 0,0,0,1);

        // Run the rendering loop until the user has attempted to close
        // the window or has pressed the ESCAPE key.
        while ( !glfwWindowShouldClose(DisplayManager.window) ) {
            // glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); // clear the framebuffer

            glfwSwapBuffers(DisplayManager.window); // swap the color buffers


            // Render here.
            rend.prepareForRendering();
            shader.start();
//            rend.renderModel(entity, shader);
            rend.renderModel(texturedModel);
            shader.stop();

            // Poll for window events. The key callback above will only be
            // invoked during this call.
            glfwPollEvents();
        }
    }
}

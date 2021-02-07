import Models.ModelLoader;
import Shaders.java.StaticShader;

import java.io.IOException;

import static org.lwjgl.glfw.Callbacks.*;
import static org.lwjgl.glfw.GLFW.*;

public class Main {

    // The window handle
    private long window;

    public void run() throws IOException {

        DisplayManager.init();
        MainGameLoop.loop();

        // Free the window callbacks and destroy the window
        glfwFreeCallbacks(window);
        glfwDestroyWindow(window);

        // Terminate GLFW and free the error callback
        Models.ModelLoader loader = new ModelLoader();
        StaticShader shader = new StaticShader();
        loader.cleanUp();
        shader.cleanUp();

        glfwTerminate();
        glfwSetErrorCallback(null).free();
    }

    public static void main(String[] args) throws IOException {
        new Main().run();
    }

}
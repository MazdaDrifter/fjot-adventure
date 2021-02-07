package Models;

import Entities.RawEntity;
import Shaders.java.StaticShader;
import Utilities.Calculations;
import org.joml.Matrix4f;
import org.lwjgl.opengl.GL30;

public class ModelRenderer {

    // Called once every frame. Prepare for rendering.
    public void prepareForRendering(){
        GL30.glClear(GL30.GL_COLOR_BUFFER_BIT);
        GL30.glClearColor(1, 0, 0, 1);
    }

    public void renderModel(TexturedModel texturedModel){
//        RawModel model = entity.getModel();
        RawModel model = texturedModel.getRawModel();
        GL30.glBindVertexArray(model.getVaoID());
        GL30.glEnableVertexAttribArray(0);
//        Matrix4f transformationMatrix = Calculations.createTransformationMatrix(entity.getPos(), entity.getRotX(), entity.getRotY(), entity.getRotZ(),
//                entity.getScl());
//        shader.loadTransMat(transformationMatrix);
        /// glDrawElements arguments = what array type?,  no of vertices, type of data given, indices index.
        GL30.glDrawElements(GL30.GL_TRIANGLES, model.getVertexCount(), GL30.GL_UNSIGNED_INT,0);
        GL30.glDisableVertexAttribArray(0);
        GL30.glBindVertexArray(0);
    }

}

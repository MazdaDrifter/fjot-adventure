package Utilities;

import org.joml.Matrix4f;
import org.joml.Vector3f;

public class Calculations {
    public static Matrix4f createTransformationMatrix(Vector3f translation, float rx, float ry,
                                                      float rz, float scale)
    {
        Matrix4f matrix4f = new Matrix4f();
        matrix4f.translate(translation, matrix4f);
        matrix4f.rotate((float)Math.toRadians(rx), new Vector3f(1,0,0), matrix4f);
        matrix4f.rotate((float)Math.toRadians(ry), new Vector3f(0,1,0), matrix4f);
        matrix4f.rotate((float)Math.toRadians(rz), new Vector3f(0,0,1), matrix4f);
        matrix4f.scale(new Vector3f(scale,scale,scale), matrix4f);
        return matrix4f;
    }
}

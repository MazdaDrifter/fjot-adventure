package Entities;

import Models.ModelLoader;
import Models.RawModel;
import org.joml.Vector3f;

public class RawEntity {

    private RawModel model; // Supposed to be TexturedModel.
    private Vector3f pos;
    private float rotX, rotY, rotZ;
    private float scl;


    public RawEntity(RawModel model, Vector3f pos, float rotX, float rotY, float rotZ, float scl) {
        this.model = model;
        this.pos = pos;
        this.rotX = rotX;
        this.rotY = rotY;
        this.rotZ = rotZ;
        this.scl = scl;
    }

    /*Move the entity around.*/
    public void increasePos(float dx, float dy, float dz){
        this.pos.x+=dx;
        this.pos.y+=dy;
        this.pos.z+=dz;
    }

    public void increaseRot(float dx, float dy, float dz){
        this.rotX+=dx;
        this.rotY+=dy;
        this.rotZ+=dz;
    }

    public RawModel getModel() {
        return model;
    }

    public Vector3f getPos() {
        return pos;
    }

    public float getRotX() {
        return rotX;
    }

    public float getRotY() {
        return rotY;
    }

    public float getRotZ() {
        return rotZ;
    }

    public float getScl() {
        return scl;
    }
}

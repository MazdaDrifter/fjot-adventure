package Models;

public class RawModel {

    private int vaoID;
    private int vertexCount;

    /*Constructor of RawModel*/
    public RawModel(int vaoID, int vertexCount){

        //Construct variables.
        this.vaoID = vaoID;
        this.vertexCount = vertexCount;
    }

    public int getVaoID() {
        return vaoID;
    }

    public int getVertexCount() {
        return vertexCount;
    }

}

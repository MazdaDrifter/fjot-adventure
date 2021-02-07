package Models;

import Textures.Texture;

public class TexturedModel {

    private RawModel rawModel;
    private Texture tex;

    public TexturedModel(RawModel rawModel, Texture texture) {
        this.rawModel = rawModel;
        this.tex = texture;
    }

    public RawModel getRawModel() {
        return rawModel;
    }

    public Texture getTex() {
        return tex;
    }
}

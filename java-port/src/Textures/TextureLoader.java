package Textures;

import Models.ModelLoader;
import de.matthiasmann.twl.utils.PNGDecoder;
import org.lwjgl.opengl.GL11;
import org.lwjgl.opengl.GL30;

import java.io.IOException;
import java.nio.ByteBuffer;

// Ref: https://stackoverflow.com/questions/41901468/load-a-texture-within-opengl-and-lwjgl3-in-java/41902221
public class TextureLoader {
    public static Texture textureLoader(String filename) throws IOException {

        // load png file.
        PNGDecoder decoder = new PNGDecoder(Texture.class.getResourceAsStream(filename));

        // Create byte buff enough to store RGBA values.
        ByteBuffer buffer = ByteBuffer.allocateDirect(4 * decoder.getWidth() * decoder.getHeight());

        // Decode.
        decoder.decode(buffer, decoder.getWidth()*4, PNGDecoder.Format.RGBA);

        // Flip buffer so it's ready to be read.
        buffer.flip();

        // Create tex.
        int id = GL30.glGenTextures();

        // Bind tex.
        GL30.glBindTexture(GL30.GL_TEXTURE_2D, id);

        // Give openGL instructions to unpack bytes.
        GL30.glPixelStorei(GL30.GL_UNPACK_ALIGNMENT, id);

        // Set tex parameters.
        GL30.glTexParameterf(GL30.GL_TEXTURE_2D, GL30.GL_TEXTURE_MIN_FILTER, GL30.GL_LINEAR);
        GL30.glTexParameterf(GL30.GL_TEXTURE_2D, GL30.GL_TEXTURE_MAG_FILTER, GL30.GL_LINEAR);

        // Upload texture.
        GL30.glTexImage2D(GL30.GL_TEXTURE_2D, 0, GL30.GL_RGBA, decoder.getWidth(), decoder.getHeight(), 0,
                GL30.GL_RGBA, GL30.GL_UNSIGNED_BYTE, buffer);

        // Generate tex map.
        GL30.glGenerateMipmap(GL30.GL_TEXTURE_2D);

        return new Texture(id);
    }
}

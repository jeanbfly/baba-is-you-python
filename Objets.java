private class Objects
{
    private byte x;
    private byte y;
    private byte dir;
    public static String type;
    
    public boolean move(byte _x, byte _y) // vérifie si le mouvement est possible et bouge si possible
    {
    
    }
    
    private void set_position(byte _x, byte _y, byte _dir)
    {
        x = _x;
        y = _y;
        dir = _dir;
    }
    
    private byte get_position()
    {
        return [x, y, dir];
    }
    
    public String get_type()
    {
        return type;
    }
}

public class Materials extends Objects
{
	private String[] properties;
	
    public Materials(byte _x, byte _y, byte _dir, String type)
    {
        set_position(_x, _y, _dir);
    }
    
    public String get_properties()
    {
    
    }
}

public class Texts extends Objects
{
    public static void light()
    {
    
    }
}

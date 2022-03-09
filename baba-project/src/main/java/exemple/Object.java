import java.util.ArrayList;

public class Object
{
    private int coorX, coorY;
    private String desc;
    private int dir;
    
    /**
    * This is the constructor which initializes the first variables.
    *
    * @param _coorX - the coordinate X of the object.
    * @param _coorY - the coordinate Y of the object.
    * @param _desc - the description of the object.
    * @param _dir - the direction of the object.
    * @author the whole team.
    */
    protected Object(int _coorX, int _coorY, String _desc, int _dir)
    {
        coorX = _coorX;
        coorY = _coorY;
        desc = _desc;
        dir = _dir;
    }
    
    /**
    * This is the method which makes you get the coordinate X.
    *
    * @param args Unused.
    * @return the coordinate X of the object.
    * @author the whole team.
    */
    public int getCoorX()
    {
        return coorX;
    }
    
    /**
    * This is the method which makes you get the coordinate Y.
    *
    * @param args Unused.
    * @return the coordinate Y of the object.
    * @author the whole team.
    */ 
    public int getCoorY()
    {
        return coorY;
    }
    
    /**
    * This is the method which updates the coordinate X of the object.
    *
    * @param _coorX - The new coordinate X.
    * @return nothing.
    * @author the whole team.
    */
    public void setCoorX(int _coorX)
    {
        coorX = _coorX;
    }
    
    /**
    * This is the method which updates the coordinate Y of the object.
    *
    * @param _coorY -The new coordinate Y.
    * @return nothing.
    * @author the whole team.
    */
    public void setCoorY(int _coorY)
    {
        coorY = _coorY;
    }

    /** 
    * This is the method which makes you get the description of the object.
    *
    * @param args Unused.
    * @return the description of the object.
    * @author the whole team.
    */
    public String getDesc()
    {
        return desc;
    }

    /** 
    * This is the method which updates the description of the object.
    *
    * @param _desc -the new description of the object.
    * @return nothing.
    * @author the whole team.
    */
    public void setDesc(String _desc)
    {
        desc = _desc;
    }
}

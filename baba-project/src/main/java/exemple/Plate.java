public class Plate
{
    private int width, heigth;
    private Object[][][] plate;

    public Plate(String _fileName)
    {

    }
    
    //On a la possibilité d'utiliser les <p> pour aérer la docu et on doit mettre les réf de nos inspirations pour le code s'il y en a.
    
    /**
    * This is the method which gets the width of the screen.
    *
    * @param args Unused.
    * @return the width of the screen.
    * @author the whole team.
    */
    public int getWidth()
    {
        return width;
    }

    /**
    * This is the method which gets the height of the screen.
    *
    * @param args Unused.
    * @return the height of the screen.
    * @author the whole team.
    */
    public int getHeight()
    {
        return heigth;
    }

    private boolean canMove(Object _obj, int _dir)
    {
        return true;
    }

    /**
    * This is the method which enables to move the object.
    *
    * @param _obj - the object that we want to move.
    * @param _dir - the direction that the player chooses.
    * @return nothing.
    * @author the whole team.
    */
    public void move(Object _obj, int _dir)
    {

    }

    /**
    * This is the method which enables to know if the party is won.
    *
    * @param args Unused.
    * @return boolean.
    * @author the whole team.
    */
    public boolean isWin()
    {
        return true;
    }

    public void gameSave()
    {

    }

    public void editSave()
    {

    }
}

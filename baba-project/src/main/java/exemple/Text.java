public class Text extends Object
{
    private boolean stateShine;
    //constructeur
    public Text(int _coorX, int _coorY, String _desc, int _dir)
    {
        super(_coorX, _coorY, _desc, _dir);
        stateShine = false;
    }
    
    // savoir s'il faut faire briller les règles
    public boolean getStateShine()
    {
        return stateShine;
    }
    
    // fais briller les règles actives
    public void invertStateShine()
    {
        stateShine = !stateShine;
    }
}

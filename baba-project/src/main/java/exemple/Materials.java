import java.util.ArrayList;

public class Materials extends Object
{   
    private ArrayList<String> prop;
    
    //constructeur
    public Materials(int _coorX, int _coorY, String _desc, int _dir, ArrayList<String> _prop)
    {
        super(_coorX, _coorY, _desc, _dir);
        prop = _prop;
    }

	// valeur en moins
    public Materials(int _coorX, int _coorY, String _desc, ArrayList<String> _prop)
    {
        super(_coorX, _coorY, _desc, 0);
        prop = _prop;
    }

	//obtenir prop
    public ArrayList<String> getProp()
    {
        return prop;
    }
    
	//modifier prop
    public void addProp(String _prop)
    {
        boolean flag = true;

        for(int i = 0; i < prop.size(); i++)
        {
            if(prop.get(i).equals(_prop))
            {
                flag = false;
            }
        }

        if(flag)
        {
            prop.add(_prop);
        }
    }

	//modifier prop
    public void delProp(String _prop)
    {
        int i = 0;

        while(i < prop.size())
        {
            if(prop.get(i).equals(_prop))
            {
                prop.remove(i);
            }

            i++;
        }
    }
}

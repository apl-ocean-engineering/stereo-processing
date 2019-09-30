# calibration_helper
Helper package for loading, saving, and storing of calbiration vlaues for cv2 impage processing. 

## Codebase

### "intrinsic_extrinsic.py"
Main module. Loads yaml file which contains relative or absoute paths of calibration values (see calibrationConfig.yaml).  

Format is: Matrix: [Load(bool), path (string)]  
Where matrix is name of intrinsic/extrinsic matracies, load is bool value for load or not to load (if not sepcified, assumed False), and path points to location of saved path. If a '/' is added to the front of the path, it signals absolute. Otherwise, path is assumed to be relative to a base path. base_path defaults to base folder location, and can be specified upon Loader class initalization.  

Module also support calculation of projection and rectification matracies, if proper values are known.  


Supported matrix types are:  
1. K1/K2
   * Intrnsic matricies for camera1/2 (3x3)
2. d1/d2
   * distortion coeffs for camera1/2 (1x5)
3. R
   * Extrinsic rotation matrix (3x3)
4. t
   * Extrinsic translation matrix (3x1)
5. P1/P2
   * Projection matracies for camera1/2 (3x4)
5. R1/R2
   * Rectification matracies for camera1/2 (3x3)

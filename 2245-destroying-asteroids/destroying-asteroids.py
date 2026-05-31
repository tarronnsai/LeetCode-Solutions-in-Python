class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # Sort asteroids from smallest to largest to absorb mass greedily
        asteroids.sort()
        
        for asteroid in asteroids:
            # If the planet is smaller than the current smallest asteroid, it fails
            if mass < asteroid:
                return False
            # Otherwise, absorb the asteroid's mass
            mass += asteroid
            
        return True

#tarronnsaiadabala